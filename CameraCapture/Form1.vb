Imports AForge
Imports AForge.Video
Imports AForge.Video.DirectShow
Imports System.IO
Imports System.Threading.Tasks
Imports System
Public Class Form1
    Dim CAMERA As VideoCaptureDevice
    Dim bmp As Bitmap
    Private Sub Form1_Load(sender As Object, e As EventArgs) Handles MyBase.Load

    End Sub

    Private Sub Button1_Click(sender As Object, e As EventArgs) Handles Button1.Click
        Dim cameras As VideoCaptureDeviceForm = New VideoCaptureDeviceForm
        If cameras.ShowDialog() = Windows.Forms.DialogResult.OK Then
            CAMERA = cameras.VideoDevice
            AddHandler CAMERA.NewFrame, New NewFrameEventHandler(AddressOf Capture)
            CAMERA.Start()
        End If
    End Sub
    Private Sub Capture(sender As Object, eventArgs As NewFrameEventArgs)
        bmp = DirectCast(eventArgs.Frame.Clone(), Bitmap)
        PictureBox1.Image = DirectCast(eventArgs.Frame.Clone(), Bitmap)
    End Sub
    Private Sub Button2_Click(sender As Object, e As EventArgs) Handles Button2.Click
        PictureBox2.Image = PictureBox1.Image
    End Sub

    Private Sub Button3_Click(sender As Object, e As EventArgs) Handles Button3.Click
        Dim programFiles As String = Environment.GetEnvironmentVariable("ProgramFiles")
        Dim programPath As String = IO.Path.Combine(programFiles, "Test", "Test.exe")
        SaveFileDialog1.DefaultExt = ".jpg"
        If SaveFileDialog1.ShowDialog = Windows.Forms.DialogResult.OK Then
            Dim imagePath As String = SaveFileDialog1.FileName
            PictureBox2.Image.Save(imagePath, Imaging.ImageFormat.Jpeg)
            Dim exeFilePath As String = System.IO.Path.Combine(My.Application.Info.DirectoryPath, "Test.exe")
            Dim arguments As String = String.Format("""{0}""", imagePath)
            Process.Start(exeFilePath, arguments)
        End If
    End Sub

    Private Sub Form1_FormClosing(sender As Object, e As FormClosingEventArgs) Handles MyBase.FormClosing
        RemoveHandler CAMERA.NewFrame, AddressOf Capture
        CAMERA.SignalToStop()
        Dim task As Task = Task.Run(Sub()
                                        CAMERA.WaitForStop()
                                    End Sub)

    End Sub
End Class
